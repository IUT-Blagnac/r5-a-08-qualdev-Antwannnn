echo Running tests...
docker run --rm password-generator-tests

set exit_code=%errorlevel%

if %exit_code% == 0 (
    echo ✅ Tests réussis!
) else (
    echo ❌ Tests échoués avec le code de sortie %exit_code%
)

exit /b %exit_code%