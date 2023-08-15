<script>
	import SoftStrong from "../components/SoftStrong.svelte";
	import T2 from "../components/T2.svelte";
	import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
	<title>Matheus Avellar</title>
</svelte:head>

<main>
	<section class="profile">
		<a href="/eu/eu-500x500.jpg">
			<picture>
				<source media="(max-width: 600px)" srcset="/eu/eu-100x100.jpg">
				<img src="/eu/eu-200x200.jpg" alt="Fotografia de mim em um campo florido.">
			</picture>
		</a>
	</section>
	<section>
		<p> Olá! </p>
		<p>
			Eu sou <SoftStrong>Matheus Avellar</SoftStrong>, e esse é um dos meus
			cantinhos na internet!
		</p>
		<p>
			Se é o que você procura, veja aqui meu
			<a href="/files/cv-matheusavellar-pt.pdf">currículo</a>.
		</p>
	</section>
	<T2>Quem sou eu</T2>
	<section>
		<ul>
			<li>Cientista da computação e programador (com foco em web);</li>
			<li>Mestrando na <a href="https://www.cos.ufrj.br/">PESC</a>/COPPE, na UFRJ;</li>
			<li>Arqueólogo digital amador;</li>
			<li>Colecionador de inutilidades;</li>
			<li>Defensor de moedas de 1 centavo;</li>
			<li>Evangelista de tênis sem cadarço;</li>
			<li>Conselheiro de epígrafes;</li>
			<li>Fã de <a href="https://www.imdb.com/title/tt2543164/">Arrival (2016)</a>.</li>
		</ul>
	</section>
</main>
<Footer/>

<style>
section ~ section {
	margin-top: 1rem;
}
.profile {
	float: right;
	margin: 0 0 1rem 1rem;
}
.profile img {
	border-radius: 8px;
	box-shadow: var(--shadow-elevation-medium);
}
ul {
	padding-left: 1.5rem;
}
li {
	list-style-type: circle;
	padding-left: .25rem;
}
</style>