# v2. File-Based Targets (`make` Decides What's Stale)

all: plots/mean.png

data/raw/%.npy data/bias/%.npy data/dark/%.npy data/flat/%.npy:
	./scripts/mkobs

results/ref/%.npy: data/%/f000.npy
	./scripts/mkref $$(basename $$(dirname $<)) $$(dirname $<)

results/%.npy: data/raw/%.npy results/ref/bias.npy results/ref/dark.npy results/ref/flat.npy
	./scripts/calmini $<

plots/mean.png: results/f000.npy
	./scripts/mkplt $<

clean:
	rm -rf results plots

clean-all:
	rm -rf data results plots
