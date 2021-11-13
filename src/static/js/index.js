let currentpage = 1;
let totalPages = 4;

let temp = currentpage/totalPages;

$(".inner").css("width", `calc(${temp}*100%)`);

$(".forward").click((e) => { 
    e.preventDefault();
    if(currentpage >= totalPages) return;
    console.log("Clicked");
    $(".sliders").css("transform", `translateY(calc(-${currentpage}*100%))`);
    currentpage = currentpage+1;
    temp = currentpage/totalPages;
    $(".inner").css("width", `calc(${temp}*100%)`);
});

$(".backward").click((e) => {
    e.preventDefault();
    if(currentpage <= 1) return;
    console.log("Clicked");
    $(".sliders").css("transform", `translateY(calc(${-currentpage + 2}*100%))`);
    currentpage = currentpage - 1;
    temp = currentpage/totalPages;
    $(".inner").css("width", `calc(${temp}*100%)`);
});

window.setInterval( () => {
    if (currentpage == 1) {
        $(".backward").css("opacity", "0");
    }
    else{
        $(".backward").css("opacity", "1");  
    }

    if(currentpage == totalPages){
        $('.forward').css("opacity", "0");

    }
    else{
        $('.forward').css("opacity", "1"); 
    }
}, 0.5);
