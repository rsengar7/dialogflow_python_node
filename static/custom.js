// Initialise Pusher
const pusher = new Pusher('a1ec41ad3b1e5c17e958', {
    cluster: 'ap2',
    encrypted: true
});

// Subscribe to movie_bot channel
const channel = pusher.subscribe('priyanka-madam');

// bind new_message event to movie_bot channel
channel.bind('new_message', function (data) {
    console.log(data)
    // Append human message
    $('.chat-container').append(`
        <div class="chat-message col-md-5 human-message">
            ${data.human_message}
        </div>
    `)

    // Append bot message
    $('.chat-container').append(`
        <div class="chat-message col-md-5 offset-md-7 bot-message">
        ${data.bot_message}
        </div>
    `)
});



$(function () {

    function submit_message(message) {

        $.post("/send_message", {
            message: message,
            socketId: pusher.connection.socket_id,
        }, handle_response);

        function handle_response(data) {

            // append the bot repsonse to the div
            console.log(data.message[0].buttons);
            var object = data.message[0].buttons;
            var buttons = '';
            for (const value in object) {
                console.log(object[value].title);
                console.log(object[value].payload);
                buttons += `<button class="customBtn" data-val='${object[value].payload}'>${object[value].title}</button>`;
            }
            console.log(buttons);
            $('.chat-container').append(`
                <div class="chat-message col-md-5 offset-md-7 bot-message">
                    ${data.message[0].text}
                    ${buttons}
                </div>
            `)

            $("#chat-container-id").animate({ scrollTop: $('#chat-container-id').height() }, 300);
            // remove the loading indicator
            $("#loading").remove();
        }
    }

    $(document).on('click', '.customBtn', function () {
        var val = $(this).attr('data-val');
        var text = $(this).text();
        $('#input_message').val(val);
        $('.chat-container').append(`
            <div class="chat-message col-md-5 human-message">
                ${text}
            </div>
        `)

        // loading 
        $('.chat-container').append(`
            <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
                <b>...</b>
            </div>
        `)

        // clear the text input 
        $('#input_message').val('')

        // send the message
        submit_message(val);
    })

    $('#target').on('submit', function (e) {
        e.preventDefault();
        const input_message = $('#input_message').val()
        // return if the user does not enter any text
        if (!input_message) {
            return
        }

        $('.chat-container').append(`
            <div class="chat-message col-md-5 human-message">
                ${input_message}
            </div>
        `)

        // loading 
        $('.chat-container').append(`
            <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
                <b>...</b>
            </div>
        `)

        // clear the text input 
        $('#input_message').val('')

        // send the message
        submit_message(input_message);

    });
});