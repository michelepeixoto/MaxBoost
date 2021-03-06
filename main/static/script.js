window.addEventListener('resize', function(event){
    var div = document.getElementById("page-width");
    div.innerHTML = window.innerWidth;
    var signin = document.getElementById("signin");
    if (signin.style.display == "inherit"){
        showSignin();
    }

});

window.addEventListener('load', function(event){
    var div = document.getElementById("page-width");
    div.innerHTML = "LOADED";
    var featured = document.getElementsByClassName("featured");
    for (i=0; i<featured.length; i++){
        featured[i].style.height = document.getElementById("most-pl1").clientHeight + 50 + "px";
    }
});

function showElement(element_id){
    document.getElementById(element_id).style.display = "inherit";
}

function hideElement(element_id){
    document.getElementById(element_id).style.display = "none";
}

function showOnline(){
    showElement("show-online");
    showElement("show-online-btns");
}

function hideOnline(){
    hideElement("show-online");
    hideElement("show-online-btns");
}

function showSignin(){
    var signin = document.getElementById("signin");
    var signin_btn = document.getElementById("signin-btn");
    var coor = signin_btn.getBoundingClientRect();
    signin.style.left = coor.x + "px";
    signin.style.top = coor.bottom + "px";
    signin.style.display = "inherit";
    signin_btn.style.backgroundColor = "#d8d8d8";
    signin_btn.style.borderRadius = "8px 8px 0 0";
}

function hideSignin(){
    hideElement("signin");
    document.getElementById("signin-btn").style.backgroundColor = "transparent";
}

function moveItems(items, dir){
    var pic_urls = document.getElementById("game-pic-urls").innerHTML.replace(new RegExp("\\s", 'g'), "").split("game_pics");
    if (items == "games"){
        games = document.getElementsByClassName("game");
        for (i=0; i<games.length; i++){
            img_src = games[i].src.replace(/[\w\d/.:]*(?=game_pics)/g, "");
            for (ii=1; ii<pic_urls.length; ii++){
                if ("game_pics" + pic_urls[ii] == img_src){
                    if (dir == "left"){
                        if (ii == 1){
                            games[i].src = "/media/game_pics" + pic_urls[pic_urls.length - 1];
                        }
                        else {
                        games[i].src = "/media/game_pics" + pic_urls[ii - 1];
                        }
                    }
                    else if (dir == "right"){
                        if (ii == pic_urls.length - 1){
                            games[i].src = "/media/game_pics" + pic_urls[1];
                        }
                        else {
                        games[i].src = "/media/game_pics" + pic_urls[ii + 1];
                        }
                    }
                }
            }
        }
    }
}

function showStats(stat_table){
    stat_tables = document.getElementsByClassName("stat-table");
    for (i=0; i<stat_tables.length; i++){
        stat_tables[i].style.display = "none";
    }
    show_table = document.getElementById(stat_table);
    show_table.style.display = "inherit";
}