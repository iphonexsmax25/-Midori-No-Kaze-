// Elements to be alterted
let submit_button = document.getElementById("submit");
let dialog_box = document.getElementById("dialog");
let chat_entry = document.getElementById("entry");

function send_response() {
    // Get response from the end-user
    let response = chat_entry.value;
    add_dialog(response, true)
    chat_entry.value = ""

    // TO-DO: Connect to Python's process_data function.
    // alert(response);

    // Send response back
    add_dialog("processed(" + response + ")", false);
}

function add_dialog(text, from_user) {
    // TO-DO: Alter to match chatbot style.
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

// Initialize with bot's greeting.
add_dialog("Hello! Please ask me anything about food nutritions!", false);