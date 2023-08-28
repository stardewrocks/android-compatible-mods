<script lang="ts">
    
    export let blur = '8px';
    export let mode: 'dark' | 'light' = 'dark';

</script>

<div class="blurrer {mode}" style="filter: blur({blur})"></div>

<style lang="scss">
    .blurrer {
        z-index: -1;
        
        position: fixed;
        inset: 0;

        width: 100%;
        height: 100%;

        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .dark {
        background-color: rgba(0, 0, 0, 0.7);
        background-image: url('$lib/images/darkmode_bg_640x400.png');
    }
</style>