// Store all BibTeX entries in one place
const bibtexEntries = {
    'crawley2025households': `@article{crawley2025households,
  title={{Do Households Substitute Intertemporally? 10 Structural Shocks That Suggest Not}},
  author={Crawley, Edmund S.},
  journal={Unpublished Manuscript},
  year={2025}
}`,
    'crawley2024income': `@techreport{crawley2024income,
  title={{Income Shocks and Their Transmission into Consumption}},
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
  title={{Welfare and Spending Effects of Consumption Stimulus Policies}},
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
    'crawley2022parsimonious': `@techreport{crawley2022parsimonious,
  title={{A Parsimonious Model of Idiosyncratic Income}},
  author={Crawley, Edmund and Holm, Martin Blomhoff and Tretvoll, H{\aa}kon},
  year={2022},
  month={May},
  number={2022-026},
  series={Finance and Economics Discussion Series},
  institution={Board of Governors of the Federal Reserve System},
  type={Finance and Economics Discussion Series},
  url={https://doi.org/10.17016/FEDS.2022.026},
  doi={10.17016/FEDS.2022.026}
}`,
    'crawley2023consumption': `@article{crawley2023consumption,
Author = {Crawley, Edmund and Kuchler, Andreas},
Title = {{Consumption Heterogeneity: Micro Drivers and Macro Implications}},
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
title = {{In search of lost time aggregation}},
journal = {Economics Letters},
volume = {189},
year = {2020},
doi = {https://doi.org/10.1016/j.econlet.2020.108998},
author = {Edmund Crawley}
}`,
    'carroll2021modeling': `@article{carroll2021modeling,
  title={{Modeling the Consumption Response to the CARES Act}},
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
Title = {{Sticky Expectations and Consumption Dynamics}},
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
  title={{A Note on the Asymptotic Properties of the Two-Sector Robinson-Solow-Srinivasan Model}},
  author={Crawley, Edmund},
  journal={Economic Theory Bulletin},
  year={2025},
  note={Forthcoming}
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