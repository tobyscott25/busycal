<script setup>
	import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
	<header>
		<div class="wrapper">
		<nav>
			<RouterLink to="/">Home</RouterLink>
			<RouterLink to="/signin">Sign In</RouterLink>
			<RouterLink to="/register">Register</RouterLink>
			<RouterLink to="/about">About</RouterLink>
		</nav>
		</div>
	</header>

	<RouterView />
</template>

<style scoped>
	nav {
		@apply bg-gray-800 text-3xl font-bold text-white no-underline
	}
	nav a {
		@apply 
	}
</style>