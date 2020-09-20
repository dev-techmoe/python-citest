from jsonip import cli
from pytest import mark

@mark.asyncio
async def test_cli():
    resp = await cli.get_ip()
    assert resp != None