// Elements to be alterted
let send_button = document.getElementById("send");
let dialog_box = document.getElementById("dialog");
let chat_entry = document.getElementById("entry");

function send_response() {
    // Get response from the end-user
    let response = chat_entry.value;
    add_dialog(response, true)

    // TO-DO: Connect to Python's process_data function.
    alert(response);

    // Send response back
    add_dialog(response, false);
}

function add_dialog(text, from_user) {
    const tbox = document.createElement("p")
    let message
    if (from_user) {
        message = document.createTextNode("Me: " + text)
    }
    else {
        message = document.createTextNode("Bot: " + text)
    }
    tbox.appendChild(message)
    dialog_box.appendChild(tbox)
}