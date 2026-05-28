// Store all BibTeX entries in one place
const bibtexEntries = {
    'crawley2025households': `@unpublished{crawley2026household,
  author = {Crawley, Edmund and Gamber, William},
  title = {Household Consumption Does Not Respond Directly to Interest Rates: Evidence From 10 Macroeconomic Shocks},
  year = {2026},
  note = {Manuscript}
}`,
    'crawley2024income': `@techreport{crawley2024income,
  title={Income Shocks and Their Transmission into Consumption},
  author={Crawley, Edmund and Theloudis, Alexandros},
  year={2024},
  number={2024-038},
  series={Finance and Economics Discussion Series},
  institution={Board of Governors of the Federal Reserve System},
  type={Finance and Economics Discussion Series},
  url={https://doi.org/10.17016/FEDS.2024.038},
  doi={10.17016/FEDS.2024.038}
}`,
    'carroll2023welfare': `@techreport{carroll2023welfare,
  title={Welfare and Spending Effects of Consumption Stimulus Policies},
  author={Carroll, Christopher and Crawley, Edmund and Frankovic, Ivan and Tretvoll, H{\aa}kon},
  year={2023},
  month={January},
  number={2023-002},
  series={Finance and Economics Discussion Series},
  institution={Board of Governors of the Federal Reserve System},
  type={Finance and Economics Discussion Series},
  url={https://doi.org/10.17016/FEDS.2023.002},
  doi={10.17016/FEDS.2023.002}
}`,
    'crawley2022parsimonious': `@article{crawley2025parsimonious,
  title={A Parsimonious Model of Idiosyncratic Income},
  author={Crawley, Edmund and Holm, Martin Blomhoff and Tretvoll, H{\aa}kon},
  journal={International Economic Review},
  year={2025},
  note={Forthcoming},
  doi={10.1111/iere.70041},
  url={https://doi.org/10.1111/iere.70041}
}`,
    'crawley2023consumption': `@article{crawley2023consumption,
Author = {Crawley, Edmund and Kuchler, Andreas},
Title = {Consumption Heterogeneity: Micro Drivers and Macro Implications},
Journal = {American Economic Journal: Macroeconomics},
Volume = {15},
Number = {1},
Year = {2023},
Month = {January},
Pages = {314–41},
DOI = {10.1257/mac.20200352},
URL = {https://www.aeaweb.org/articles?id=10.1257/mac.20200352}
}`,
    'crawley2020losttime': `@article{crawley2020losttime,
title = {In Search of Lost Time Aggregation},
journal = {Economics Letters},
volume = {189},
year = {2020},
doi = {https://doi.org/10.1016/j.econlet.2020.108998},
author = {Edmund Crawley}
}`,
    'carroll2021modeling': `@article{carroll2021modeling,
  title={Modeling the Consumption Response to the CARES Act},
  author={Carroll, Christopher D. and Crawley, Edmund and Slacalek, Jiri and White, Matthew N.},
  journal={International Journal of Central Banking},
  volume={17},
  number={1},
  month={March},
  year={2021},
  pages={107--141},
  url={https://www.ijcb.org/journal/ijcb21q1a4.htm}
}`,
    'carroll2020sticky': `@article{carroll2020sticky,
Author = {Carroll, Christopher D. and Crawley, Edmund and Slacalek, Jiri and Tokuoka, Kiichi and White, Matthew N.},
Title = {Sticky Expectations and Consumption Dynamics},
Journal = {American Economic Journal: Macroeconomics},
Volume = {12},
Number = {3},
Year = {2020},
Month = {July},
Pages = {40–76},
DOI = {10.1257/mac.20180286},
URL = {https://www.aeaweb.org/articles?id=10.1257/mac.20180286}
}`,
    'crawley2025asymptotic': `@article{crawley2025asymptotic,
  title={A Note on the Asymptotic Properties of the Two-Sector Robinson-Solow-Srinivasan Model},
  author={Crawley, Edmund},
  journal={Economic Theory Bulletin},
  year={2025},
  month={March}
  DOI = {https://doi.org/10.1007/s40505-025-00290-4}
}`,
    'crawley2023svbfailure': `@techreport{crawley2023svbfailure,
  title={Failure of Silicon Valley Bank Reduced Local Consumer Spending but Had Limited Effect on Aggregate Spending},
  author={Crawley, Edmund and Doh, Taeyoung and Shin, Minchul},
  institution={Federal Reserve Bank of Kansas City},
  type={Economic Bulletin},
  year={2023},
  month={September},
  day={6},
  url={https://www.kansascityfed.org/research/economic-bulletin/failure-of-silicon-valley-bank-reduced-local-consumer-spending-but-had-limited-effect-on-aggregate-spending/}
}`,
    'crawley2023winners': `@techreport{crawley2023winners,
  title={Winners and Losers from Recent Asset Price Changes},
  author={Crawley, Edmund and Gamber, William},
  institution={Board of Governors of the Federal Reserve System},
  type={FEDS Notes},
  year={2023},
  month={May},
  day={12},
  url={https://doi.org/10.17016/2380-7172.3287},
  doi={10.17016/2380-7172.3287}
}`,    
'crawley2022substitutability': `@techreport{crawley2022substitutability,
  title={Substitutability between Balance Sheet Reductions and Policy Rate Hikes: Some Illustrations and a Discussion},
  author={Crawley, Edmund and Gagnon, Etienne and Hebden, James and Trevino, James},
  institution={Board of Governors of the Federal Reserve System},
  type={FEDS Notes},
  year={2022},
  month={June},
  day={3},
  url={https://doi.org/10.17016/2380-7172.3147},
  doi={10.17016/2380-7172.3147}
}`,
'carroll2018comment': `@article{carroll2018comment,
author = {Carroll, Christopher D. and Crawley, Edmund},
title = {Comment on When Inequality Matters for Macro and Macro Matters for Inequality. What’s Wrong with Macroeconomics, and Can This Paper Fix It?},
journal = {NBER Macroeconomics Annual},
volume = {32},
number = {},
pages = {76-92},
year = {2018},
doi = {10.1086/696047},
URL = {https://doi.org/10.1086/696047},
eprint = {https://doi.org/10.1086/696047}
}`
};

// Function to copy BibTeX to clipboard
function copyBibtex(id, button) {
    const bibtexText = bibtexEntries[id];
    
    navigator.clipboard.writeText(bibtexText)
        .then(() => {
            // Change button text temporarily
            const originalText = button.textContent;
            button.textContent = "Copied!";
            setTimeout(() => {
                button.textContent = originalText;
            }, 2000);
        })
        .catch(err => {
            console.error('Failed to copy: ', err);
            alert('Failed to copy. Please select and copy manually.');
        });
}
