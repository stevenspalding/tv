// url: http://172.16.215.142
// name: s9_flixhub

vidlink = document.getElementById("vidlink");
cats = vidlink.children;
out = [];

for (var i = 0; i < cats.length; i++) {
  category = cats[i].className;
  ch = cats[i].firstChild;
  url = "http://172.16.215.142/" + ch.dataset.link;
  img = ch.firstChild.src;
  title = img.split("/").slice(-1)[0];
  title = title.replace(".jpg", "").replace(".jpeg", "").replace(".png", "");
  entry = {
    title: title,
    logo: img,
    url: url,
    category: category,
  };
  out.push(entry);
}
out;
