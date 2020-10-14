<script>
  import T2 from "../components/T2.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
  <title>Projetos | Matheus Avellar</title>
</svelte:head>

<main>
  <section>
    <T2> Projetos </T2>
    <article>
      <figure style="background-image:url(/preview/o-amendoim.png)"></figure>
      <h3> O Amendoim </h3>
      <p>
        Blogzinho em que eu faço pesquisas e escrevo sobre coisas que eu
        descubro.
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://o.amendo.im/">o.amendo.im</a>.
      </p>
    </article>
    <article>
      <figure style="background-image:url(/preview/bandwidth-humana.png)"></figure>
      <h3> Bandwidth Humana </h3>
      <p>
        Quão eficiente seria uma conexão utilizando humanos como transmissores
        de informação? Se um humano lendo e escrevendo substituísse, por exemplo,
        o 4G, quão menos eficiente seria?
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://matheusavellar.github.io/bandwidth-humana/">matheusavellar.github.io/bandwidth-humana/</a>;
        <a href="https://github.com/MatheusAvellar/bandwidth-humana">código-fonte</a>.
      </p>
    </article>
    <article>
      <figure style="background-image:url(/preview/troca-grana.png)"></figure>
      <h3> Troca Grana </h3>
      <p>
        Pequeno jogo infantil para crianças aprenderem e treinarem a somar
        valores presentes em cédulas do real. Foi mencionado no <a href="https://www.cp2.g12.br/blog/labtijuca1/2019/11/21/sistema-monetario/"
        rel="noopener noreferrer">blog do Colégio Pedro II</a>.
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://avellar.ml/trocagrana/">avellar.ml/trocagrana</a>.
      </p>
    </article>
    <article>
      <figure style=""></figure>
      <h3> File Extension Watch Dog (fewd) </h3>
      <p>
        Programa proof-of-concept que automaticamente converte arquivos quando
        eles são renomeados (i.e. renomear `arquivo.jpg` para `arquivo.png`
        realmente converte a imagem para PNG).
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://github.com/MatheusAvellar/fewd">código-fonte</a>.
      </p>
    </article>
    <article>
      <figure style="background-image:url(/preview/adobe-logo-generator.png)"></figure>
      <h3> Adobe Logo Generator </h3>
      <p>
        Gerador de pseudo-logotipos que se parecem com logotipos de produtos da
        Adobe (ex. Photoshop, Illustrator, etc).
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://matheusavellar.github.io/adobe-logos/">matheusavellar.github.io/adobe-logos</a>;
        <a href="https://github.com/MatheusAvellar/adobe-logos">código-fonte</a>.
      </p>
    </article>
    <article>
      <figure style="background-image:url(/preview/plates.png)"></figure>
      <h3> Plates </h3>
      <p>
        Site que verifica se palavras podem ser escritas como placas de
        trânsito.
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://matheusavellar.github.io/plates/">matheusavellar.github.io/plates</a>;
        <a href="https://github.com/MatheusAvellar/plates">código-fonte</a>.
      </p>
    </article>
    <article>
      <figure style="background-image:url(/preview/centavo.png)"></figure>
      <h3> Centavo </h3>
      <p>
        Vale a pena se abaixar para pegar uma moeda de R$0,01?
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://matheusavellar.github.io/centavo/">matheusavellar.github.io/centavo</a>;
        <a href="https://github.com/MatheusAvellar/centavo">código-fonte</a>.
      </p>
    </article>
    <article>
      <figure style="background-image:url(/preview/dun-machine.png)"></figure>
      <h3> Dun Machine </h3>
      <p>
        Site inspirado em <a rel="noopener noreferrer"
        href="https://twitter.com/i/status/1077978238314520577">um tweet</a>
        sobre a quantidade de "dun"s em músicas.<br>…é mais legal do que soa,
        eu juro.
      </p>
      <p>
        <strong>Links:</strong>
        <a href="https://matheusavellar.github.io/dun-machine/">matheusavellar.github.io/dun-machine</a>;
        <a href="https://github.com/MatheusAvellar/dun-machine">código-fonte</a>.
      </p>
    </article>
  </section>
</main>
<Footer/>

<style>
article {
  padding-left: 1rem;
  margin: 2.5rem 0;
}
article + article {
  margin-top: 1rem;
}
h3 {
  font-size: 1.2rem;
}
strong {
  font-weight: 500;
}
figure {
  background-size: cover;
  height: 7.5rem;
  width: 20rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  margin: 0 0 0.5rem -2px;
  padding: 0;
  background-position: center;
  background-repeat: no-repeat;

  background-color: #f2f2f2;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%23dfdfdf' fill-opacity='1'%3E%3Cpath d='M0 38.59l2.83-2.83 1.41 1.41L1.41 40H0v-1.41zM0 1.4l2.83 2.83 1.41-1.41L1.41 0H0v1.41zM38.59 40l-2.83-2.83 1.41-1.41L40 38.59V40h-1.41zM40 1.41l-2.83 2.83-1.41-1.41L38.59 0H40v1.41zM20 18.6l2.83-2.83 1.41 1.41L21.41 20l2.83 2.83-1.41 1.41L20 21.41l-2.83 2.83-1.41-1.41L18.59 20l-2.83-2.83 1.41-1.41L20 18.59z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
</style>