function showModal(event, name, description, imageUrl) {
    event.preventDefault();

    document.querySelector('#modal-title').textContent = name;
    document.querySelector('#modal-description').textContent = description;
    document.querySelector('#modal-image').src = imageUrl;
    document.querySelector('#modal').style.display = 'flex';
}

function closeModal() {
    document.querySelector('#modal').style.display = 'none';
}