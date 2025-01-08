echo "Running tests..."
docker run --rm password-generator-tests

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "✅ Tests réussis!"
else
    echo "❌ Tests échoués avec le code de sortie $exit_code"
fi

exit $exit_code