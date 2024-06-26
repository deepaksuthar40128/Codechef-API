const axios = require('axios');
const jsdom = require("jsdom");
const express = require('express');
const cors = require('cors');
const { JSDOM } = jsdom;

const app = express();


app.use(cors());
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views',);
app.use(express.static(__dirname + '/static'));
app.get('/heatmap/:handle', (req, res) => {
    let theme = req.query.theme == 'night' ? 'night' : 'day';
    res.render('heatmap', { handle: req.params.handle, theme });
})
app.get('/rating/:handle', (req, res) => {
    res.render('rating', { handle: req.params.handle });
})

app.get('/:handle', async (req, res) => {
    try {
        let data = await axios.get(`https://www.codechef.com/users/${req.params.handle}`);
        let heatMapDataCursour1 = data.data.search("var userDailySubmissionsStats =") + "var userDailySubmissionsStats =".length;
        let heatMapDataCursour2 = data.data.search("'#js-heatmap") - 9;
        let heatDataString = data.data.substring(heatMapDataCursour1, heatMapDataCursour2)
        let headMapData = JSON.parse(heatDataString)
        let allRating = data.data.search("var all_rating = ") + "var all_rating = ".length;
        let allRating2 = data.data.search("var current_user_rating =") - 6;
        let ratingData = JSON.parse(data.data.substring(allRating, allRating2))
        let dom = new JSDOM(data.data);
        let document = dom.window.document;
        res.status(200).send({
            success: true,
            profile: document.querySelector('.user-details-container').children[0].children[0].src,
            name: document.querySelector('.user-details-container').children[0].children[1].textContent,
            currentRating: parseInt(document.querySelector(".rating-number").textContent),
            highestRating: parseInt(document.querySelector(".rating-number").parentNode.children[4].textContent.split('Rating')[1]),
            countryFlag: document.querySelector('.user-country-flag').src,
            countryName: document.querySelector('.user-country-name').textContent,
            globalRank: parseInt(document.querySelector('.rating-ranks').children[0].children[0].children[0].children[0].innerHTML),
            countryRank: parseInt(document.querySelector('.rating-ranks').children[0].children[1].children[0].children[0].innerHTML),
            stars: document.querySelector('.rating').textContent || "unrated",
            heatMap: headMapData,
            ratingData
        });
    } catch (err) {
        res.send({ success: false, error: err });
    }
});

app.get('/', (req, res) => {
    res.render('home')
    // res.status(200).send("Hi you are at right endpoint just add /handle_of_user at the end of url Github-repo(https://github.com/deepaksuthar40128/Codechef-API) Thanks for 🌟");
});

const PORT = process.env.PORT || 8800;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
