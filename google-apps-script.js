/**
 * Google Apps Script för att ta emot quiz-resultat
 *
 * INSTRUKTIONER FÖR LÄRAREN:
 * 1. Öppna Google Sheets och skapa ett nytt kalkylblad
 * 2. Gå till Extensions > Apps Script
 * 3. Ta bort befintlig kod och klistra in denna kod
 * 4. Klicka på Deploy > New deployment
 * 5. Välj "Web app" som typ
 * 6. Sätt "Execute as" till "Me"
 * 7. Sätt "Who has access" till "Anyone"
 * 8. Klicka Deploy
 * 9. Kopiera Web App URL och klistra in den i HTML-filen
 */

// Namn på bladet där sammanfattningen ska sparas
const SUMMARY_SHEET_NAME = 'Resultatsammanfattning';
// Namn på bladet där detaljerade svar ska sparas
const DETAILS_SHEET_NAME = 'Detaljerade Svar';

function doPost(e) {
  try {
    // Parse incoming data
    const data = JSON.parse(e.postData.contents);

    // Get or create the spreadsheet
    const ss = SpreadsheetApp.getActiveSpreadsheet();

    // Save summary
    saveSummary(ss, data);

    // Save detailed answers
    saveDetails(ss, data);

    return ContentService.createTextOutput(JSON.stringify({
      'status': 'success',
      'message': 'Resultat sparade'
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    Logger.log('Error: ' + error.toString());
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'error',
      'message': error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function saveSummary(ss, data) {
  let sheet = ss.getSheetByName(SUMMARY_SHEET_NAME);

  // Create sheet if it doesn't exist
  if (!sheet) {
    sheet = ss.insertSheet(SUMMARY_SHEET_NAME);

    // Add headers
    const headers = [
      'Tidpunkt',
      'Elevens Namn',
      'Antal Frågor',
      'Rätt Svar',
      'Fel Svar',
      'Procent',
      'Betyg',
      'Tid'
    ];

    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);

    // Format headers
    sheet.getRange(1, 1, 1, headers.length)
      .setFontWeight('bold')
      .setBackground('#667eea')
      .setFontColor('#ffffff');

    // Freeze header row
    sheet.setFrozenRows(1);

    // Auto-resize columns
    for (let i = 1; i <= headers.length; i++) {
      sheet.autoResizeColumn(i);
    }
  }

  // Add new row
  const newRow = [
    data.timestamp,
    data.studentName,
    data.totalQuestions,
    data.correctAnswers,
    data.incorrectAnswers,
    data.percentage + '%',
    data.grade,
    data.timeSpent
  ];

  sheet.appendRow(newRow);

  // Color code based on grade
  const lastRow = sheet.getLastRow();
  let color = '#ffffff';

  if (data.grade === 'A') color = '#d4edda';
  else if (data.grade === 'B') color = '#d1ecf1';
  else if (data.grade === 'C') color = '#fff3cd';
  else if (data.grade === 'D') color = '#ffe0b2';
  else if (data.grade === 'E') color = '#ffccbc';
  else if (data.grade === 'F') color = '#f8d7da';

  sheet.getRange(lastRow, 1, 1, newRow.length).setBackground(color);
}

function saveDetails(ss, data) {
  let sheet = ss.getSheetByName(DETAILS_SHEET_NAME);

  // Create sheet if it doesn't exist
  if (!sheet) {
    sheet = ss.insertSheet(DETAILS_SHEET_NAME);

    // Add headers
    const headers = [
      'Tidpunkt',
      'Elevens Namn',
      'Fråga Nr',
      'Fråga',
      'Elevens Svar',
      'Rätt Svar',
      'Resultat'
    ];

    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);

    // Format headers
    sheet.getRange(1, 1, 1, headers.length)
      .setFontWeight('bold')
      .setBackground('#667eea')
      .setFontColor('#ffffff');

    // Freeze header row
    sheet.setFrozenRows(1);

    // Auto-resize columns
    for (let i = 1; i <= headers.length; i++) {
      sheet.autoResizeColumn(i);
    }
  }

  // Add all detailed answers
  data.details.forEach(detail => {
    const newRow = [
      data.timestamp,
      data.studentName,
      detail.questionNumber,
      detail.question,
      detail.studentAnswer,
      detail.correctAnswer,
      detail.isCorrect ? 'Rätt' : 'Fel'
    ];

    sheet.appendRow(newRow);

    // Color code based on correctness
    const lastRow = sheet.getLastRow();
    const color = detail.isCorrect ? '#d4edda' : '#f8d7da';
    sheet.getRange(lastRow, 1, 1, newRow.length).setBackground(color);
  });
}

// Test function (optional - run this to test the script)
function testDoPost() {
  const testData = {
    postData: {
      contents: JSON.stringify({
        timestamp: new Date().toLocaleString('sv-SE'),
        studentName: 'Test Testsson',
        totalQuestions: 3,
        correctAnswers: 2,
        incorrectAnswers: 1,
        percentage: 67,
        grade: 'C',
        timeSpent: '2:30',
        details: [
          {
            questionNumber: 1,
            question: 'Testfråga 1?',
            studentAnswer: 'Svar 1',
            correctAnswer: 'Svar 1',
            isCorrect: true
          },
          {
            questionNumber: 2,
            question: 'Testfråga 2?',
            studentAnswer: 'Svar A',
            correctAnswer: 'Svar B',
            isCorrect: false
          },
          {
            questionNumber: 3,
            question: 'Testfråga 3?',
            studentAnswer: 'Svar X',
            correctAnswer: 'Svar X',
            isCorrect: true
          }
        ]
      })
    }
  };

  doPost(testData);
}
