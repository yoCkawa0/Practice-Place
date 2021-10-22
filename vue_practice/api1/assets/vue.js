var vm = new Vue({
    el: "#app",
    data: {
        results: null,
        keyword: '',
        params: {
            q: '',
            part: 'snippet',
            type: 'video',
            maxResults: '10',
            key: 'API key'
        }
    },
    methods: {
        searchMovies: function () {
            this.params.q = this.keyword;
            var self = this;
            axios
                .get('https://www.googleapis.com/youtube/v3/search', {
                    params: this.params
                })
                .then(function (res) {
                    self.results = res.data.items;
                })
                .catch(function (err) {
                    console.log(err);
                });
        }
    }
});