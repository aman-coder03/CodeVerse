async function sendVoice() {
  const voiceInput = document.getElementById('voiceInput').value;

  const res = await fetch('/voice-code', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ voice: voiceInput })
  });

  const data = await res.json();
  document.getElementById('codeOutput').textContent = data.code;
}

async function getErrorResponse() {
  const errorType = document.getElementById('errorType').value;

  const res = await fetch('/error-response', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ error_type: errorType })
  });

  const data = await res.json();
  document.getElementById('funnyResponse').textContent = data.response;
}
