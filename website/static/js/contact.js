// Contact Form (Example Submission Logic)
document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("contactName").value.trim();
  const email = document.getElementById("contactEmail").value.trim();
  const message = document.getElementById("contactMsg").value.trim();

  alert(`Thank you, ${name}! We received your message:\n\n"${message}"\n\nWe will contact you at ${email}.`);
});
