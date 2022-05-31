<template>
    <form @submit.prevent="submitData">
        <h1>Sign In</h1>
        <div>
            <label for="email">Email</label>
            <input type="text" id="email" v-model="email">
            <p :class="{invisible: isValidEmail}">Please enter a valid email address.</p>
        </div>
        <div>
            <label for="password">Password</label>
            <input type="text" id="password" v-model="password">
        </div>
        <div id="options">
            <button>Sign In</button>
            <a href="#">Forgot Password?</a>
        </div>
        
    </form>
</template>

<script>
    export default {
        data () {
            return {
                email: "",
                password: ""
            }   
        },
        methods: {
            submitData() {
                //Submit data
            }
        },
        computed: {
            isValidEmail() {
                const re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                return re.test(this.email);
            }
        }
    }

</script>

<style scoped>
    form {
        @apply bg-gray-700 w-full max-w-xs rounded shadow-md px-8 pt-6 pb-8 mb-4
    }
    label {
        @apply block text-white text-sm font-bold mb-2
    }
    input {
        @apply shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight
    }
    #options {
        @apply flex items-center justify-between top-3 relative
    }
    button {
        @apply bg-purple-600 hover:bg-purple-500 py-2 px-3 rounded text-white font-bold
    }
    a {
        @apply font-bold text-purple-600
    }
    p {
        @apply text-red-600
    }
    h1 {
        @apply text-white font-bold text-center text-xl
    }
    .invisible {
    visibility: hidden;
  }
</style>