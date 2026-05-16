/**
 * AI Interior Designer - Main JavaScript
 * Handles file upload, drag & drop, and UI interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // ===================================
    // File Upload Handling
    // ===================================
    
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const selectFileBtn = document.getElementById('selectFileBtn');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const removeImageBtn = document.getElementById('removeImageBtn');
    const uploadForm = document.getElementById('uploadForm');
    
    if (selectFileBtn && fileInput) {
        // Open file dialog when clicking the select button
        selectFileBtn.addEventListener('click', function(e) {
            e.preventDefault();
            fileInput.click();
        });
        
        // Handle file selection
        fileInput.addEventListener('change', handleFileSelect);
        
        // Remove image
        if (removeImageBtn) {
            removeImageBtn.addEventListener('click', function() {
                fileInput.value = '';
                imagePreview.style.display = 'none';
                dropZone.querySelector('.drop-zone-content').style.display = 'block';
            });
        }
    }
    
    if (dropZone) {
        // Prevent default drag behaviors
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, preventDefaults, false);
            document.body.addEventListener(eventName, preventDefaults, false);
        });
        
        // Highlight drop zone when dragging over it
        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, highlight, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, unhighlight, false);
        });
        
        // Handle dropped files
        dropZone.addEventListener('drop', handleDrop, false);
        
        // Click anywhere in drop zone to open file dialog
        dropZone.addEventListener('click', function(e) {
            if (e.target === dropZone || e.target.closest('.drop-zone-content')) {
                fileInput.click();
            }
        });
    }
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    function highlight() {
        dropZone.classList.add('drag-over');
    }
    
    function unhighlight() {
        dropZone.classList.remove('drag-over');
    }
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length > 0) {
            fileInput.files = files;
            handleFileSelect();
        }
    }
    
    function handleFileSelect() {
        const file = fileInput.files[0];
        
        if (file) {
            // Validate file type
            const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
            if (!validTypes.includes(file.type)) {
                alert('Please select a valid image file (JPG, PNG, or WEBP)');
                fileInput.value = '';
                return;
            }
            
            // Validate file size (16MB max)
            const maxSize = 16 * 1024 * 1024; // 16MB in bytes
            if (file.size > maxSize) {
                alert('File size must be less than 16MB');
                fileInput.value = '';
                return;
            }
            
            // Show preview
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImg.src = e.target.result;
                imagePreview.style.display = 'block';
                dropZone.querySelector('.drop-zone-content').style.display = 'none';
            };
            reader.readAsDataURL(file);
        }
    }
    
    // ===================================
    // Form Validation
    // ===================================
    
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            if (!fileInput.files.length) {
                e.preventDefault();
                alert('Please select an image to upload');
                return false;
            }
        });
    }
    
    // ===================================
    // Smooth Scrolling
    // ===================================
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // ===================================
    // Interactive Elements
    // ===================================
    
    // Add hover effects to cards
    const cards = document.querySelectorAll('.feature-card, .style-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // ===================================
    // Auto-dismiss alerts after 5 seconds
    // ===================================
    
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // ===================================
    // Copy color codes to clipboard
    // ===================================
    
    const colorSwatches = document.querySelectorAll('.color-swatch');
    colorSwatches.forEach(swatch => {
        swatch.addEventListener('click', function() {
            const colorCode = this.querySelector('.color-code').textContent;
            navigator.clipboard.writeText(colorCode).then(() => {
                // Show temporary tooltip
                const originalText = this.querySelector('.color-code').textContent;
                this.querySelector('.color-code').textContent = 'Copied!';
                setTimeout(() => {
                    this.querySelector('.color-code').textContent = originalText;
                }, 1000);
            });
        });
    });
    
    // ===================================
    // Initialize tooltips
    // ===================================
    
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// ===================================
// Loading Animation
// ===================================

function showLoading() {
    const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    loadingModal.show();
}

function hideLoading() {
    const loadingModal = bootstrap.Modal.getInstance(document.getElementById('loadingModal'));
    if (loadingModal) {
        loadingModal.hide();
    }
}