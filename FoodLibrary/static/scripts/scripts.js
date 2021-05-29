function Hide() {
    if (document.getElementById('id_product_type').options[document.getElementById('id_product_type').selectedIndex].value === "1") {
        var labels = document.getElementsByTagName('LABEL');
        for (let i = 0; i < labels.length; i++) {
            if (labels[i].htmlFor !== '') {
                var elem = document.getElementById(labels[i].htmlFor);
                if (elem)
                    elem.label = labels[i];
            }
        }
        document.getElementById('id_produced_by').style.display = 'none';
        document.getElementById('id_ingredients').style.display = 'none';
        document.getElementById('id_produced_by').label.style.display = 'none';
        document.getElementById('id_ingredients').label.style.display = 'none';
    } else {
        document.getElementById('id_produced_by').style.display = 'block';
        document.getElementById('id_ingredients').style.display = 'block';
        document.getElementById('id_produced_by').label.style.display = 'block';
        document.getElementById('id_ingredients').label.style.display = 'block';
    }
}

window.onload = function () {
    document.getElementById('id_product_type').onchange = Hide;
};

function toggleNavbar() {
    let navbar = document.getElementById("myTopnav");
    if (navbar.className === "topnav") {
        navbar.className += " responsive";
    } else {
        navbar.className = "topnav";
    }
}