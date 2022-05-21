$(document).ready(function() {
    
    $("#feelings_submit").click(function() {
        const input = $("#feelings_input").val();
        if (input !== "") {
            processInput(input);
        } else {
            $("#feelings_response_wrapper").fadeIn();
            setTimeout(() => {
                $("#feelings_response_wrapper").fadeOut();
            }, 5000)
        }
    })

    $("#feelings_input").keypress(function(e) {
        if (e.which === 13) {
            const input = $("#feelings_input").val();
            if (input !== "") {
              processInput(input);
            } else {
              $("#feelings_response_wrapper").fadeIn();
              setTimeout(() => {
                $("#feelings_response_wrapper").fadeOut();
              }, 5000);
            }
        }
    })
    

    function processInput(input) {
        const emotionalResponses = {
            "happy": "That's great! BetaMind are happy for you!",
            "sad": "It's ok to be sad sometimes, life isn't always easy.",
            "depressed": "You need to know that you are not alone.",
            "anxious": "Go easy on yourself. Whatever you do today, let it be enough.",
            "scared": "Fear is nothing more than an obstacle that stands in the way of progress. In overcoming our fears, we can move forward. Stronger and wiser within ourselves.",
            "excited": "The future is bright, and you are on the right path!",
            "bored": "Pay attention to yourself. Some of your best ideas come out of being bored!",
            "calm": "Wonderful. We hope you keep seeing things clearly.",
            "nostalgic": "Nostalgia is a seductive liar, that insists things were better than they seemed.",
            "relieved": "Take a deep breath!",
            "disgusted": "Disgust and resolve are two of the great emotions that lead to change.",
            "amused": "The world's a playground, an amusement park!",
            "awesome": "We're really happy for you! Keep it up.",
            "confused": "Confusion is a word we have invented for an order which is not yet understood.",
            "surprised": "Surprise is the greatest gift which life can grant us!",
            "angry": "If you are patient in one moment of anger, you will escape 100 days of sorrow.",
            "satisfied": "A satisfied life is better than a 'successful' life."
        }

        const response = match(input, emotionalResponses)
        displayMessage(response)
    }

    function displayMessage(response) {
        $("#error_response").css("display", "none");
        const responseText = response;
        $("#feelings_response").text(responseText)
        $("#feelings_response_wrapper").fadeIn();

        setTimeout(() => {
            $("#feelings_response_wrapper").fadeOut(function() {
                removeContent();
                $("#error_response").css("display", "block");
            }) 
        }, 8000)

        $("#feelings_input").val("")
    }

    function match(input, obj) {
        var matched = Object.keys(obj).find(key => input.toLowerCase().search(key) > -1);
        return obj[matched] || null;
    }


    function removeContent() {
        $("#feelings_response").text("")
    }
})