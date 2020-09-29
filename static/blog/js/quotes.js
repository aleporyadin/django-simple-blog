$(document).ready(function(){
    var quotes= [
        'Logic can take you from point A to point B, and imagination can take you anywhere.',
        'It is always worth starting with something that sows doubts.',
        'Your time is limited, don\'t waste it living someone else\'s life'
    ]
    var authorQuotes=[
        'Albert Einstein',
        'Boris Strugatsky',
        'Steve Jobs'
    ]
    var randomQuotes=Math.floor(Math.random() * quotes.length); 
    $('.innerAuthorquotes').append('<i>'+authorQuotes[randomQuotes]+'  —'+'</i>');
    $('.innerTextquotes').append('<i> \" '+quotes[randomQuotes]+' \"</i>');
});
