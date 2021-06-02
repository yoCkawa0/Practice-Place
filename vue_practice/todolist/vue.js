/** Vue アプリの生成 **/
function createApp() {
    new Vue({
        el: "#wrapper",
        data: {
            filter: "inbox",
            todos: [{
                    id: 1,
                    text: "do my homework",
                    createdAt: 1622606882908, // 登録日の Unix タイムスタンプ（ミリ秒）
                    done: false // タスクが完了したかどうか
                },
                {
                    id: 2,
                    text: "clean my room",
                    createdAt: 1622506882908,
                    done: false
                },
                {
                    id: 3,
                    text: "clean my home",
                    createdAt: 1622406882908,
                    done: false
                },
                {
                    id: 4,
                    text: "go to bed",
                    createdAt: 1622306882908,
                    done: true
                },
            ]
        },

        computed: {
            todoLength: function () {
                return this.todos.length
            },
            filteredTodos: function () {
                const filter = this.filter
                return this.todos.filter(function (todo) {
                    return filter == "completed" ? todo.done : !todo.done
                })
            }
        },

        // タイムスタンプを変換
        methods: {
            formatDate: function (timestamp) {
                const date = new Date(timestamp)

                const year = date.getFullYear()
                const month = date.getMonth() + 1
                const day = date.getDate()

                return year + "." + month + "." + day
            },
            setFilter: function (filter) {
                this.filter = filter
            }
        },
    })
}

/** 初期化 **/
function initialize() {
    createApp()
}

document.addEventListener("DOMContentLoaded", initialize.bind(this))