<script lang="ts">
    import Blurrer from "$lib/Blurrer.svelte";
    import Credit from "$lib/Credit.svelte";
    
    import './global.scss';
    import '@fontsource/source-sans-pro';

</script>
    
<Blurrer blur="5px" />

<main>
    <slot />
</main>

<Credit />

<style lang="scss">
    

</style>