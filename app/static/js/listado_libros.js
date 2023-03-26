(function() {
    const btnsComprarLibro = document.querySelectorAll('.btnComprarLibro');
    let isbnLibro = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;

    btnsComprarLibro.forEach((btn) => {
        btn.addEventListener('click', function ()  {
            isbnLibro = this.id;
            confirmarCompra();
        })
    });

    const confirmarCompra = async () => {
        await fetch('http://127.0.0.1:5000/comprarLibro', {
            method: 'POST',
            mode: 'same-origin',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-TOKEN': csrf_token
            },
            body: JSON.stringify({
                'isbn': isbnLibro
            })
        }).then(response => {
            if (!response.ok) {
                console.error('Error!');
            }
            return response.json();
        }).then(data => {
            console.log('Libro comprado!');
        }).catch(error => {
            console.error(`Error ${error}`);
        });
    };
})();