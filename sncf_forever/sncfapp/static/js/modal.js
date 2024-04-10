function showModal(event, name, description, imageUrl, destination, arrive, departure) {
    event.preventDefault();

    document.querySelector('#modal-title').textContent = name;
    document.querySelector('#modal-description').textContent = description;
    document.querySelector('#modal-image').src = imageUrl;
    document.querySelector('#modal').style.display = 'flex';
    document.querySelector('#modal-departure').textContent = departure;
    document.querySelector('#modal-arrive').textContent = arrive;
    document.querySelector('#modal-destination').textContent = destination;
}

function closeModal() {
    document.querySelector('#modal').style.display = 'none';
}