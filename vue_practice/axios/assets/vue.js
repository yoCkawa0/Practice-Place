var vm = new Vue({
    el: '#app',
    data: {
        student: {}
    },
    created: function () {
        self = this;
        axios
            .get('./data/test.json')
            .then(function (res) {
                self.student = res.data;
            })
            .catch(function (err) {
                console.log(err);
            });
    }
});

var vm2 = new Vue({
    el: '#app2',
    data: {
        items: [],
        reverse: false,
        orderIcon: '▲'
    },
    computed: {
        sortedItems: function () {
            if (this.reverse) {
                return this.items.slice().sort(function (a, b) {
                    return b.price - a.price
                });
            } else {
                return this.items.slice().sort(function (a, b) {
                    return a.price - b.price;
                });
            }
        }
    },
    methods: {
        reverseOrder: function () {
            this.reverse = !this.reverse;
            if (this.reverse) {
                this.orderIcon = '▼';
            } else {
                this.orderIcon = '▲';
            }
        }
    },
    created: function () {
        self = this;
        axios
            .get('./data/item.json')
            .then(function (res) {
                self.items = res.data.items;
            })
            .catch(function (err) {
                console.log(err);
            });
    }
});