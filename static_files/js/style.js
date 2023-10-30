
    const thumbnails = document.querySelectorAll('.gallery img');
    const modal = document.getElementById('myModal');
    const modalImg1 = document.getElementById('modalImg1');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    let currentImageIndex = 0;
    
    function showImage(index) {
        modalImg1.src = thumbnails[index].src.replace('small_', 'large_'); // Örnek adlandırma
        currentImageIndex = index;
    }

    function showNextImage() {
        if (currentImageIndex < thumbnails.length - 1) {
            showImage(currentImageIndex + 1);
        }
    }

    function showPrevImage() {
        if (currentImageIndex > 0) {
            showImage(currentImageIndex - 1);
        }
    }

    thumbnails.forEach((thumbnail, index) => {
        thumbnail.addEventListener('click', () => {
            modal.style.display = 'block';
            showImage(index);
        });
    });

    nextButton.addEventListener('click', showNextImage);
    prevButton.addEventListener('click', showPrevImage);

    modal.addEventListener('click', () => {
        modal.style.display = 'none';
    });
    
    window.addEventListener('DOMContentLoaded', (event) => {
        // JavaScript kodu burada çalışacak
    });
    
    lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true
    });