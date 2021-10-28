function answer_rate(url, id, type) {
    $.ajax(url, {
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({
            "type": type,
        }),
        success: function(data) {
            let icon_up = $("#rate\\+" + id.toString());
            let icon_down = $("#rate-" + id.toString());
            const class_up = "bi-arrow-up-circle";
            const class_down = "bi-arrow-down-circle";
            if (type) {
                // Change selected rating
                if (icon_up.hasClass(class_up)) {
                    icon_up.toggleClass(class_up + " " + class_up + "-fill");
                } else if (icon_up.hasClass(class_up + "-fill")) {
                    icon_up.toggleClass(class_up + "-fill" + " " + class_up);
                }
                // Change other rating
                if (icon_down.hasClass(class_down + "-fill")) {
                    icon_down.toggleClass(class_down + "-fill" + " " + class_down);
                }
            } else {
                // Change selected rating
                if (icon_down.hasClass(class_down)) {
                    icon_down.toggleClass(class_down + " " + class_down + "-fill");
                } else if (icon_down.hasClass(class_down + "-fill")) {
                    icon_down.toggleClass(class_down + "-fill" + " " + class_down);
                }
                // Change other rating
                if (icon_up.hasClass(class_up + "-fill")) {
                    icon_up.toggleClass(class_up+ "-fill" + " " + class_up);
                }
            }
        },
    });
}
