from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

VERSION = "v1.0.4"

setup(
    name="wemeet-openapi-sdk-python",
    version=VERSION[1:],
    description="OpenAPI SDK for Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wemeet",
    author_email="wemeet@tencent.com",
    url="https://github.com/TencentCloud/wemeet-openapi-sdk-python",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
    keywords=["Wemeet", "OpenAPI SDK"],
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/TencentCloud/wemeet-openapi-sdk-python",
    },
)
