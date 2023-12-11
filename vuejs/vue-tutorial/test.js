var vueInstance = new Vue({
    el: '#app',
    data: {
        title: 'test instance VueJS',
        url: 'https://www.google.com/',
        ok: true,
        price: 200000
    },
    methods: {
        say: function(text){
            return 'Hello, ' + text
        },
        formatPrice (){
            return new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'VND' }).format(this.price)
        }
    }
})

// console.log(vueInstance);