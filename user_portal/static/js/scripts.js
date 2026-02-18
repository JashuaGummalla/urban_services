document.addEventListener("DOMContentLoaded", function() {
    // Confirm before deleting products
    const deleteLinks = document.querySelectorAll("a[href*='product/delete']");
    deleteLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            if(!confirm("Are you sure you want to delete this product?")) {
                event.preventDefault();
            }
        });
    });

    // Validate purchase input before submit
    const purchaseForms = document.querySelectorAll("form[action*='purchase']");
    purchaseForms.forEach(form => {
        form.addEventListener("submit", function(event) {
            const qtyInput = form.querySelector("input[name='quantity']");
            if(!qtyInput || parseInt(qtyInput.value)<=0) {
                alert("Please enter a quantity greater than zero to purchase.");
                event.preventDefault();
            }
        });
    });
});
