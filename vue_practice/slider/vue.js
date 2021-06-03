function createApp() {
    new Vue({
        el: "#app1",
        data: {
            currentTabIndex: 0,
            tabs: [{
                    id: 1,
                    name: "tab1",
                    content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodilaboriosam aut earum, quia modi deleniti officia perspiciatis aliquamomnis.A alias, velit aut at dolorum animi molestiae aliquid ipsamaxime ? ",
                },
                {
                    id: 2,
                    name: "tab2",
                    content: "tab2 Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodilaboriosam aut earum, quia modi deleniti officia perspiciatis aliquamomnis.A alias, velit aut at dolorum animi molestiae aliquid ipsamaxime ? ",
                },
                {
                    id: 3,
                    name: "tab3",
                    content: "tab3 Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodilaboriosam aut earum, quia modi deleniti officia perspiciatis aliquamomnis.A alias, velit aut at dolorum animi molestiae aliquid ipsamaxime ? ",
                },
                {
                    id: 4,
                    name: "tab4",
                    content: "tab4 Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodilaboriosam aut earum, quia modi deleniti officia perspiciatis aliquamomnis.A alias, velit aut at dolorum animi molestiae aliquid ipsamaxime ? ",
                }
            ]
        },
        computed: {
            currentTabContent() {
                return this.tabs[this.currentTabIndex].content
            }
        },
        methods: {
            onClick(index) {
                this.currentTabIndex = index
            }
        },
    })
    new Vue({
        el: "#app2",
        data: {
            isOpenModal: false,
        },
        methods: {
            openModal() {
                this.isOpenModal = true
            },
            closeModal() {
                this.isOpenModal = false
            },
        },
        mounted() {
            const _this = this
            document.addEventListener("click", function (event) {
                const target = event.target.closest("#modal")
                if (_this.isOpenModal && target == null) {
                    _this.closeModal()
                }
            })
        },
    })

    // app3 area
    new Vue({
        el: "#app3",
        data: {
            isOpenMenu: false,
        },
        methods: {
            openMenu() {
                this.isOpenMenu = true
            },
            closeMenu() {
                this.isOpenMenu = false
            }
        },
    })

    Vue.use(VueAwesomeSwiper)
    new Vue({
        el: "#app4",
        // data: {

        // }
    })
}

function initialize() {
    createApp()
}
document.addEventListener("DOMContentLoaded", initialize.bind(this))