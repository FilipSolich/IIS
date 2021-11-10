function answer_rate(url, id, type) {
    $.ajax(url, {
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({
            "type": type,
        }),
        success: function(data) {
            function change_points(id, num) {
                let points = $("#points-" + id.toString());
                let value = parseInt(points.text(), 10);
                value += num;
                points.text(value);
            }
            let icon_up = $("#rate\\+" + id.toString());
            let icon_down = $("#rate-" + id.toString());
            const class_up = "bi-arrow-up-circle";
            const class_down = "bi-arrow-down-circle";
            if (type) {
                // Change selected rating
                if (icon_up.hasClass(class_up)) {
                    icon_up.toggleClass(class_up + " " + class_up + "-fill");
                    change_points(id, 1);
                } else if (icon_up.hasClass(class_up + "-fill")) {
                    icon_up.toggleClass(class_up + "-fill" + " " + class_up);
                    change_points(id, -1);
                }
                // Change other rating
                if (icon_down.hasClass(class_down + "-fill")) {
                    icon_down.toggleClass(class_down + "-fill" + " " + class_down);
                    change_points(id, 1);
                }
            } else {
                // Change selected rating
                if (icon_down.hasClass(class_down)) {
                    icon_down.toggleClass(class_down + " " + class_down + "-fill");
                    change_points(id, -1);
                } else if (icon_down.hasClass(class_down + "-fill")) {
                    icon_down.toggleClass(class_down + "-fill" + " " + class_down);
                    change_points(id, 1);
                }
                // Change other rating
                if (icon_up.hasClass(class_up + "-fill")) {
                    icon_up.toggleClass(class_up+ "-fill" + " " + class_up);
                    change_points(id, -1);
                }
            }
        },
    });
}
