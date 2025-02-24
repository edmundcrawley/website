// Store all BibTeX entries in one place
const bibtexEntries = {
    'households-substitute': `@article{crawley2025households,
  title={Do Households Substitute Intertemporally? 10 Structural Shocks That Suggest Not},
  author={Crawley, Edmund S.},
  journal={Working Paper},
  year={2025}
}`,
    'income-shocks': `@article{crawley2023income,
  title={Income Shocks and their Transmission into Consumption},
  author={Crawley, Edmund S. and Theloudis, Alexandros},
  journal={Encyclopedia of Consumption},
  year={2023}
}`,
    'welfare-spending': `@article{crawley2023welfare,
  title={Welfare and Spending Effects of Consumption Stimulus Policies},
  author={Crawley, Edmund S. and Carroll, Chris and Frankovic, Ivan and Tretvoll, H{\\\aa}kon},
  journal={Federal Reserve Board FEDS Working Paper},
  year={2023}
}`,
    'asymptotic-properties': `@article{crawley2025asymptotic,
  title={A Note on the Asymptotic Properties of the Two-Sector Robinson-Solow-Srinivasan Model},
  author={Crawley, Edmund S.},
  journal={Economic Theory Bulletin},
  note={Forthcoming},
  year={2025}
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