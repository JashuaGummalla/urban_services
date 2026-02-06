document.addEventListener('DOMContentLoaded', function() {
    // Booking Form Validation
    const bookingForm = document.querySelector('form');
    // Simple check to identify booking form, generally by the date field presence
    const dateInput = document.querySelector('input[type="date"]');
    const timeInput = document.querySelector('input[type="time"]');

    if (dateInput && timeInput && bookingForm) {
        bookingForm.addEventListener('submit', function(event) {
            let isValid = true;
            const errors = [];
            
            // Date Validation
            const selectedDate = new Date(dateInput.value);
            const today = new Date();
            today.setHours(0, 0, 0, 0); // Reset time to start of day

            if (!dateInput.value) {
                errors.push("Please select a date.");
                isValid = false;
            } else if (selectedDate <= today) {
                errors.push("Booking date must be in the future.");
                isValid = false;
            }

            // Time Validation
            if (!timeInput.value) {
                errors.push("Please select a time.");
                isValid = false;
            } else {
                const [hours, minutes] = timeInput.value.split(':').map(Number);
                if (hours < 9 || hours >= 17) {
                    errors.push("Bookings are only available between 9:00 AM and 5:00 PM.");
                    isValid = false;
                }
            }

            if (!isValid) {
                event.preventDefault();
                alert(errors.join('\n'));
            }
        });
    }
});
