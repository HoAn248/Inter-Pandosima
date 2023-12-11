var vueInstance = new Vue({
    el: '#app',
    data: {
        title: 'test instance VueJS'
    },
    methods: {
        say: function(text){
            return 'Hello, ' + text
        }
    }
})

console.log(vueInstance);