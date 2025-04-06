<div class="flex flex-col gap-12">
  <div class="flex flex-grow items-center justify-center gap-1">
    <span class="bar bg-slate-950"></span>
    <span class="bar bg-slate-950"></span>
    <span class="bar bg-slate-950"></span>
  </div>

  <h3 class="text-center">Trwa generowanie diety. Proszę czekać</h3>
</div>

<style>
.bar {
  width: 12px;
  height: 64px;
  margin: 2px;
  border-radius: 1px;
  animation: bounce 0.6s infinite alternate;
  animation-delay: calc(0.2s * var(--i));
}

.bar:nth-child(1) {
  --i: 0;
}
.bar:nth-child(2) {
  --i: 1;
}
.bar:nth-child(3) {
  --i: 2;
}

@keyframes bounce {
  0% {
    transform: scaleY(0);
  }
  100% {
    transform: scaleY(1);
  }
}
</style>
