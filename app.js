const date = new Date();
const options = {
    weekday: "long",
    day: "numeric",
    year: "numeric",
    month: "long", /* if it be numeric it will show month/day/year format */
    hour: "numeric",
    minute: "numeric",
    seceond: "numeric",  /* without seceond it will show day/month/year format */
}
let now = date.toLocaleDateString("en", options)

console.log(now);

const time = new Date().toLocaleDateString("en", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
    hour: "numeric",
    minute: "numeric",
})

console.log(time);