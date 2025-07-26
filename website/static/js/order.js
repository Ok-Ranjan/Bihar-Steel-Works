// WhatsApp Order Form Submission
document.getElementById("orderForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const product = document.getElementById("product").value;
  const quantity = document.getElementById("quantity").value;
  const message = document.getElementById("message").value.trim();

  const whatsappMessage = `*Bihar Steel Works - New Order*\n\nName: ${name}\nPhone: ${phone}\nProduct: ${product}\nQuantity: ${quantity}\nAdditional Notes: ${message || "N/A"}`;

  const encodedMessage = encodeURIComponent(whatsappMessage);
  const whatsappURL = `https://wa.me/918709751861?text=${encodedMessage}`; // replace with your WhatsApp number

  window.open(whatsappURL, "_blank");
});
