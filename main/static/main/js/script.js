// load content from clicking on menu
$('nav ul li a').on('click', function (event) {
    event.preventDefault();
    let url = this.href.replace('.html', '');

    $('nav ul li').removeClass('bg-blue-700 text-white rounded-sm');
    $(this).parent().addClass('bg-blue-700 text-white rounded-sm');

    $('#container').remove();
    // $(window).load() put loader here
    $('#content').load(url).hide().fadeIn('slow');
});


// To hide dropdown when clicking anywhere on the document
$(document).on('click', function(event) {
    // If the click was not on the dropdown button or any of its descendants
    if (!$(event.target).closest('#dropdown-button').length) {
        $('#dropdown-menu').addClass('hidden');
    }
});

// dropdown menu
$('#dropdown').on('click', (event) => {
    event.stopPropagation();
    $('#dropdown-menu').toggleClass('hidden')
});

// To hide dropdown on specific keypress, e.g., ESC key
$(document).on('keydown', function(event) {
    // Check if the key pressed was 'ESC' (key code 27)
    if (event.keyCode === 27) {
        $('#dropdown-menu').addClass('hidden');
    }
});


// dropdown url
$('#dropdown-menu a').on('click', function () {
    event.preventDefault();
    let url = this.href.replace('.html', '');

    //load content after removing previous content
    $('#container').remove();
    $('#content').load(url).hide().fadeIn('slow');
});

$('#toggler').on('click', function (event) {
    event.preventDefault();
    const aside = $('aside');
    if (aside.hasClass('hidden')) {
        aside.removeClass('hidden');
        aside.addClass('absolute');
    } else {
        aside.removeClass('absolute');
        aside.addClass('hidden');
    }
});

$('#get_started').on('click', function () {
    $('#server').removeClass('hidden');
    $('#started').addClass('hidden');
})

$(document).ready(function () {
    $('#loader').fadeOut('slow');
});