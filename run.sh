# Install Jekyll and Bundler gems
gem install jekyll bundler

# Move to the project directory
cd ./my_project

# Install the dependencies in the Gemfile
bundle install

# Build the site and make it available on a local server
bundle exec jekyll serve
