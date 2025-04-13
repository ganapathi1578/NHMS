const chatbotContainer = document.getElementById('chatbotContainer');
        const chatInput = document.getElementById('chatInput');

        chatbotContainer.addEventListener('click', function() {
            this.classList.add('expanded');
            chatInput.focus();
        });

        document.addEventListener('click', function(e) {
            if (!chatbotContainer.contains(e.target)) {
                chatbotContainer.classList.remove('expanded');
            }
        });

        chatInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });