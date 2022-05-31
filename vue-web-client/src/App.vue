<script setup>
	import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
	<header>
		<div class="wrapper">
		<nav class="text-3xl font-bold underline">
			<RouterLink to="/">Home</RouterLink>
			<RouterLink to="/signin">Sign In</RouterLink>
			<RouterLink to="/register">Register</RouterLink>
			<RouterLink to="/about">About</RouterLink>
		</nav>
		</div>
	</header>

	<RouterView />
</template>