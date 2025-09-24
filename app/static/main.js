const form = document.getElementById('predict-form');
const resultEl = document.getElementById('result');

async function predict(payload) {
  const res = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `HTTP ${res.status}`);
  }
  return res.json();
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  resultEl.style.display = 'none';
  const tenure = Number(document.getElementById('tenure').value);
  const charges = Number(document.getElementById('charges').value);
  const contract = Number(document.getElementById('contract').value);
  try {
    const body = { instances: [{ tenure_months: tenure, monthly_charges: charges, contract_type: contract }] };
    const data = await predict(body);
    resultEl.innerHTML = `<strong>Prediction:</strong> ${data.predictions[0]}<br/><strong>Probability:</strong> ${data.probabilities[0].toFixed(4)}`;
    resultEl.style.display = 'block';
  } catch (err) {
    resultEl.innerHTML = `<strong>Error:</strong> ${err.message}`;
    resultEl.style.display = 'block';
  }
});
