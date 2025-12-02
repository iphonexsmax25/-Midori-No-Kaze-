document.addEventListener("DOMContentLoaded", function() {

    // grab elements
    const msgInput = document.querySelector(".chatbox-input");
    const form = document.querySelector(".chatbox-form");
    const chatArea = document.querySelector(".chatbox-content");
    const emptyMsg = document.querySelector(".chatbox-empty");
    const menuBtn = document.querySelector(".chatbox-menu-btn");
    const menu = document.querySelector(".chatbox-menu");

    // auto resize input as user types
    msgInput.addEventListener("input", function() {
        msgInput.style.height = "auto"; 
        if (msgInput.scrollHeight > 120) {
            msgInput.style.height = "120px";
        } else {
            msgInput.style.height = msgInput.scrollHeight + "px";
        }
    });

    // menu stuff
    menuBtn.onclick = function(e) {
        e.stopPropagation();
        menu.classList.toggle("show");
    };

    document.onclick = function(e) {
        if (!menuBtn.contains(e.target)) {
            menu.classList.remove("show");
        }
    };

    // handle form submit
    form.onsubmit = async function(e) {
        e.preventDefault();
        
        const txt = msgInput.value.trim();
        if (txt.replace(/\s/g, '') == '') return; // basic check

        // add user msg
        addMessage(txt, 'sent');
        msgInput.value = '';
        msgInput.style.height = 'auto';
        
        if (emptyMsg) emptyMsg.style.display = 'none';

        // call backend
        try {
            const res = await fetch('http://localhost:8000/reply', {
                method: 'POST',
                headers: {'Content-Type': 'text/plain; charset-UTF-8"'},
                body: txt
            });
            const reply = await res.text();
            console.log(reply)
            addMessage(reply, 'received');
        } catch(err) {
            addMessage('Error connecting to server', 'received');
            console.log(err);
        }
    };

    // add message to chat
    function addMessage(text, type) {
        const now = new Date();
        const time = now.getHours().toString().padStart(2,'0') + ':' + now.getMinutes().toString().padStart(2,'0');
        
        // escape html - probably overkill but whatever | yeah it is overkill lol
        // text = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        
        const div = document.createElement('div');
        div.className = 'chatbox-message-item ' + type;
        div.innerHTML = '<div>' + text.replace(/\n/g, '<br>') + '</div><span class="chatbox-message-time">' + time + '</span>';
        
        chatArea.appendChild(div);
        chatArea.scrollTop = chatArea.scrollHeight; // scroll down
    }

});