function answer_rate(url, type) {
    $.post(url, {
        'type': type,
    })
}
