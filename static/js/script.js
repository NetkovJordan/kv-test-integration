// Professional JavaScript for enhanced interactions
document.addEventListener('DOMContentLoaded', function() {
    console.log('Professional Flask app loaded');

    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Only prevent default if it's an anchor link (you can add logic here)
        });
    });

    // Add loading animation to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.tagName === 'BUTTON' && this.type === 'submit') {
                this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
                this.disabled = true;
                // Simulate form submission (in real app, remove this)
                setTimeout(() => {
                    this.innerHTML = '<i class="fas fa-check me-2"></i>Sent!';
                    setTimeout(() => {
                        this.innerHTML = '<i class="fas fa-paper-plane me-2"></i>Send Message';
                        this.disabled = false;
                    }, 2000);
                }, 2000);
            }
        });
    });

    // Parallax effect for hero section (simple implementation)
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero-section');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });

    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});